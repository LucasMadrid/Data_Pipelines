from flask import Flask, Response, stream_with_context
import time
import uuid
import random

app = Flask(__name__)


@app.route("/large_data_request/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """retunrs N rows of data"""
    def generator():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.001)

            transaction_id = uuid.uuid4()
            print(f'trans id: {transaction_id}')
            user_id = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            yield f"('{transaction_id}', '{user_id}', {amount})\n"

    return Response(stream_with_context(generator()))

if __name__ == "__main__":
    app.run(debug=True)