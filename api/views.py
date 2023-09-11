from Customer.models import Customer
from rest_framework.views import APIView
from Cartsystem.models import Cart
from inventory.models import Product
from Order.models import Order
from .serializers import CustomerSerializer,CartSerializer,ProductSerializer,OrderSerializer
from rest_framework.response  import Response
from rest_framework import status,generics

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()  # Correct the case to 'all()'
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Correct the case
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Correct the case
class CustomerDetailView(APIView):
    def get (self , request , id,format=None ):
        customer= Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put (self , request , id,format=None ):
        customer= Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer,request.data)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= CustomerSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status.http_201_created)
      
        else:
           return Response(serializer.data,status.http_400_BAD_REQUEST)
       
       
    def delete(self, request,id,format=None):
       customer=Customer.objects.get(id=id,status=status.HTTP_204_CONTENT)
        
class CartListAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def add_product_to_basket(self, request, *args, **kwargs):
        cart = self.get_object()

        # Extract the product data from the request data
        product_data = request.data.get('Product') 
        # You might need to adjust this based on your request structure

        if not product_data:
            return Response({'error': 'Product data is missing'}, 
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(pk=product_data['id'])
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'},
                            status=status.HTTP_404_NOT_FOUND)

        cart.products.add(product)

        cart_serializer = CartSerializer(cart)

        return Response(cart_serializer.data, status=status.HTTP_200_OK)
    
    
    
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()  # Correct the case to 'all()'
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Correct the case
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Correct the case
class ProductDetailView(APIView):
    def get (self , request , id,format=None ):
        product= Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put (self , request , id,format=None ):
        product= Product.objects.get(id=id)
        serializer = ProductSerializer(product,request.data)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status.http_201_created)
      
        else:
           return Response(serializer.data,status.http_400_BAD_REQUEST)
       
       
    def delete(self, request,id,format=None):
       product=Product.objects.get(id=id,status=status.HTTP_204_CONTENT)
       
       
class OrderListView(APIView):
    def get(self, request):
        order = Order.objects.all()  # Correct the case to 'all()'
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Correct the case
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Correct the case
  
        
class OrderDetailView(APIView):
    def get (self , request , id,format=None ):
        order= Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def put (self , request , id,format=None ):
        order= Order.objects.get(id=id)
        serializer = OrderSerializer(order,request.data)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= OrderSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status.http_201_created)
      
        else:
           return Response(serializer.data,status.http_400_BAD_REQUEST)
       
       
    def delete(self, request,id,format=None):
       order=Order.objects.get(id=id,status=status.HTTP_204_CONTENT)
       
       
       class AddToCartView(APIView):
           def post(self,request, format=None):
               cart_id =request.data["cart_id"]
               product_id =request.data["product_id"]
               cart =Cart.objects.get(id=cart_id)
               updated_cart=cart.add_product(product)
               serializer=CartSerializer(updated_cart)
               return Response(serializer.data)

               