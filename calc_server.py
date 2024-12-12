import grpc
from concurrent import futures
import calc_pb2
import calc_pb2_grpc

class CalcServicer(calc_pb2_grpc.CalcServicer):
    def Add(self, request, context:grpc.ServicerContext):
        # Perform the addition operation
        result = request.x + request.y
        return calc_pb2.CalcResp(result=result)
    def Sub(self, request, context):
        result = request.x - request.y
        return calc_pb2.CalcResp(result=result)
    def Mul(self, request, context):
        result = request.x * request.y
        return calc_pb2.CalcResp(result=result)
    def Div(self, request, context):
        if request.y == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Division by zero is not allowed.")
            return calc_pb2.CalcResp(result=0)
        result = request.x / request.y
        return calc_pb2.CalcResp(result=result)
    

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalcServicer_to_server(CalcServicer(), server)

    # Listen on port 50051
    server.add_insecure_port('[::]:50051')
    print("Server is running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()