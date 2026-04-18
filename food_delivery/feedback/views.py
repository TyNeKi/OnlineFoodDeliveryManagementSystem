from datetime import datetime

from django.shortcuts import render

from .models import Complaint, Delivery, Review
from orders.models import Order
from restaurant.models import Restaurant
from accounts.models import Customer, Admin, Driver


def feedback_app_view(request):
    context = {
        'created': [],
        'errors': [],
    }

    if request.method == 'POST':
        order_id = request.POST.get('complaint_order_id')
        customer_id = request.POST.get('complaint_customer_id')
        admin_id = request.POST.get('complaint_admin_id')
        description = request.POST.get('complaint_description')
        complaint_status = request.POST.get('complaint_status')

        delivery_order_id = request.POST.get('delivery_order_id')
        driver_id = request.POST.get('delivery_driver_id')
        pickup_time = request.POST.get('delivery_pickup_time')
        delivery_time = request.POST.get('delivery_delivery_time')
        delivery_status = request.POST.get('delivery_status')

        review_customer_id = request.POST.get('review_customer_id')
        review_restaurant_id = request.POST.get('review_restaurant_id')
        review_order_id = request.POST.get('review_order_id')
        review_rating = request.POST.get('review_rating')
        review_comment = request.POST.get('review_comment')

        if order_id and customer_id and admin_id and description and complaint_status:
            try:
                complaint = Complaint.objects.create(
                    orderID=Order.objects.get(orderID=order_id),
                    customerID=Customer.objects.get(customerID=customer_id),
                    adminID=Admin.objects.get(adminID=admin_id),
                    description=description,
                    status=complaint_status,
                )
                context['created'].append(f'Complaint {complaint.complaintID} created')
            except Exception as exc:
                context['errors'].append(f'Complaint error: {exc}')

        if delivery_order_id and delivery_status:
            try:
                delivery = Delivery.objects.create(
                    orderID=Order.objects.get(orderID=delivery_order_id),
                    driverID=Driver.objects.get(driverID=driver_id) if driver_id else None,
                    pickupTime=datetime.fromisoformat(pickup_time) if pickup_time else None,
                    deliveryTime=datetime.fromisoformat(delivery_time) if delivery_time else None,
                    deliveryStatus=delivery_status,
                )
                context['created'].append(f'Delivery {delivery.deliveryID} created')
            except Exception as exc:
                context['errors'].append(f'Delivery error: {exc}')

        if review_customer_id and review_restaurant_id and review_order_id and review_rating and review_comment:
            try:
                review = Review.objects.create(
                    customerID=Customer.objects.get(customerID=review_customer_id),
                    restaurantID=Restaurant.objects.get(restaurantID=review_restaurant_id),
                    order=Order.objects.get(orderID=review_order_id),
                    rating=int(review_rating),
                    comment=review_comment,
                )
                context['created'].append(f'Review {review.reviewID} created')
            except Exception as exc:
                context['errors'].append(f'Review error: {exc}')

    return render(request, 'feedback/feedback_app.html', context)
