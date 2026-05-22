import requests
payload = {
    "Nama" : "Maulana Abdul Aziz",
    "Kelas" : "1IA01",
    "NPM" : "50425612"
}

parameter = {
    'id' : 2
}
addpost = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    data=payload
)

getPostById = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=parameter
)

if (addpost.status_code == 201):
    print("Data Berhasil Dikirim")
    print(addpost.text)
else: 
    print("Data Gagal Dikirim")

print(getPostById.text)
print(getPostById.status_code)