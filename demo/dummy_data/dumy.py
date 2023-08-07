status = "pending"
data = ""
instance = (status, data)

if instance.status == "pending":
    instance.status = "in_aile"
elif instance.status == "in_aile":
    instance.status = "picking_from_aile"
elif instance.status == "picking_from_aile":
    instance.status = "packaging_items"
elif instance.status == "packaging_items":
    instance.status = "to_departure_door"
elif instance.status == "to_departure_door":
    instance.status = "in_departure_door"
elif instance.status == "in_departure_door":
    instance.status = "ready_to_fly"

# packing > scanning >