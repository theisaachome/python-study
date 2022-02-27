phone_brand= {
            "id": "1",
            "name": "Nokia",
            "logo": "www.example/nokia",
}

newBrand = phone_brand.copy();
newBrand["year"]=1990;
print(phone_brand);
print(newBrand)

secondBrand= dict(newBrand);
print(secondBrand);