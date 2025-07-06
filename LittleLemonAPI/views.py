from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from .models import (
    Category,
    MenuItem,
    Cart,
    Order,
)
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    CartSerializer,
    OrderSerializer,
)

# 1. AssignManager
class AssignManager(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        username = request.data.get("username")
        try:
            user = User.objects.get(username=username)
            manager_group = Group.objects.get(name="manager")
            user.groups.add(manager_group)
            return Response({"message": f"{username} added to manager group."})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        except Group.DoesNotExist:
            return Response({"error": "Manager group not found"}, status=500)

# 2. CategoryCreateView
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

# 3. MenuItemCreateView
class MenuItemCreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

# 4. MenuItemListView
class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

# 5. CategoryListView
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# 6. AddToCartView
class AddToCartView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 7. CartListView
class CartListView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

# 8. PlaceOrderView
class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            return Response({"error": "Cart is empty"}, status=400)
        total = sum([item.menuitem.price * item.quantity for item in cart_items])
        order = Order.objects.create(
            user=request.user,
            total=total,
            status="pending"
        )
        cart_items.delete()
        return Response({"message": "Order placed successfully."})

# 9. MyOrdersView
class MyOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

# 10. AssignDeliveryCrew
class AssignDeliveryCrew(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        username = request.data.get("username")
        try:
            user = User.objects.get(username=username)
            delivery_group = Group.objects.get(name="delivery_crew")
            user.groups.add(delivery_group)
            return Response({"message": f"{username} added to delivery crew."})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        except Group.DoesNotExist:
            return Response({"error": "Delivery crew group not found"}, status=500)

# 11. AssignOrderToDelivery
class AssignOrderToDelivery(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        order_id = request.data.get("order_id")
        username = request.data.get("username")
        try:
            order = Order.objects.get(id=order_id)
            user = User.objects.get(username=username)
            order.delivery_crew = user
            order.save()
            return Response({"message": f"Order {order_id} assigned to {username}."})
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

# 12. DeliveryOrdersView
class DeliveryOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(delivery_crew=self.request.user)

# 13. UpdateOrderStatus
class UpdateOrderStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get("order_id")
        try:
            order = Order.objects.get(id=order_id, delivery_crew=request.user)
            order.status = "delivered"
            order.save()
            return Response({"message": "Order marked as delivered."})
        except Order.DoesNotExist:
            return Response({"error": "Order not found or not assigned to you"}, status=404)
