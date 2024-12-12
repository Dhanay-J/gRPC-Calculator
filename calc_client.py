import grpc
import calc_pb2
import calc_pb2_grpc

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calc_pb2_grpc.CalcStub(channel)

        # Create a request
        x = 10
        y = 150
        request = calc_pb2.CalcReq(x=x, y=y)

        # Perform the Add RPC and get the response
        response = stub.Add(request)

        print(f"The sum of {x} and {y} is: {response.result}")

if __name__ == '__main__':
    run()