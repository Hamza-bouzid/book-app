import boto3
from starlette.responses import JSONResponse

from src.models.ApiResponse import ApiResponse
from src.models.Book import Book
from src.repositories.db import dynamodb
from botocore.exceptions import ClientError


class DynamoDB:
    def __init__(self, book_table: str):
        self.book_table = book_table
        self.table = dynamodb.Table(book_table)
        self.db = boto3.client('dynamodb')

    def create_book(self, book: dict):
        self.db.put_item(TableName=self.book_table, Item=book)
        return True

    def get_book(self, book_id: str) -> ApiResponse:
        response = self.db.get_item(
            TableName=self.book_table,
            Key={
                'id': {'S': book_id}
            }
        )

        if 'Item' not in response:
            raise Exception("Book not found")

        return Book.from_dynamodb_item(response['Item'])

    def get_books(self, ):
        books = self.db.scan(TableName=self.book_table)
        if "Items" not in books:
            raise Exception("No books found")
        return [Book.from_dynamodb_item(item) for item in books["Items"]]

    def update_book(self, book_id: str, book: dict) -> JSONResponse:
        try:

            update_expression = "set "
            expression_attribute_values = {}

            for key, value in book.items():
                update_expression += f"{key} = :{key}, "
                expression_attribute_values[f":{key}"] = value

            update_expression = update_expression.rstrip(", ")

            response = self.table.update_item(
                Key={"id": book_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW",
            )

            return response
        except ClientError as e:
            return JSONResponse(
                status_code=500, content={"message": e.response["Error"]["Message"]}
            )

    def delete_book(self, book_id: str):
        try:
            response = self.table.delete_item(Key={"id": book_id})

            return response
        except ClientError as e:
            return JSONResponse(
                status_code=500, content={"message": e.response["Error"]["Message"]}
            )
