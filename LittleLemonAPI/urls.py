from django.urls import path
from .views import (
    AssignManager,
    CategoryCreateView,
    MenuItemCreateView,
    MenuItemListView,
    CategoryListView,
    AddToCartView,
    CartListView,
    PlaceOrderView,
    MyOrdersView,
    AssignDeliveryCrew,
    AssignOrderToDelivery,
    DeliveryOrdersView,
    UpdateOrderStatus,
)

urlpatterns = [
    path("assign-manager/", AssignManager.as_view()),
    path("add-category/", CategoryCreateView.as_view()),
    path("add-menu-item/", MenuItemCreateView.as_view()),
    path("menu-items/", MenuItemListView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("cart/add/", AddToCartView.as_view()),
    path("cart/", CartListView.as_view()),
    path("order/place/", PlaceOrderView.as_view()),
    path("my-orders/", MyOrdersView.as_view()),
    path("assign-delivery-crew/", AssignDeliveryCrew.as_view()),
    path("assign-order/", AssignOrderToDelivery.as_view()),
    path("delivery-orders/", DeliveryOrdersView.as_view()),
    path("update-order-status/", UpdateOrderStatus.as_view()),
]
