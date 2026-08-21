from django.shortcuts import render, get_object_or_404

from .models import ParkingLot



def parking_list(request):
    parkings = ParkingLot.objects.all()

    return render(
        request,
        "parking/parking_list.html",
        {"parking": parkings},
    )

def parking_detail(request, pk):
    parking = get_object_or_404(ParkingLot, pk=pk)
    operations = parking.operations.all()
    return render(
        request,
        "parking/parking_detail.html",
        {
        "parking": parking,
            "operations": operations,
        },
    )
