## Presentation 

This is a website that serves as a "showcase" for a car dealer, named ***CarHub***.

The backend of this site has been built using ***Django***, while the frontend has been built using ***Vue CLI*** and ***Bootstrap 5***. 
The backend and the frontend are two separated entities, in the sense that the backend runs on _localhost:8000_ and the frontend runs on _localhost:8080_. The frontend communicates with the backend through API enpoints exposed by the backend using ***Django Rest Framework***. 

A single car is represented by the following model: 

```Python
class Car(models.Model):
    make = models.CharField(max_length=70)
    model = models.CharField(max_length=70)
    version = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=70)
    year = models.CharField(max_length=70)
    gear = models.CharField(max_length=70)
    fuel = models.CharField(max_length=70)
    mileage = models.CharField(max_length=70)
    power = models.CharField(max_length=70)
    optionals = models.TextField()
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    miniature = models.FileField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    showcase = models.BooleanField(default=False)

    def __str__(self):
        return self.make + " " + self.model 
```

The endpoints to create, update, retrieve and delete a car have been created using the following viewset: 

```Python
class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer
    lookup_field = 'slug' 
    pagination_class = CustomPagination 
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else: 
            permission_classes = [] 
        return [permission() for permission in permission_classes]
```


The dealer can publish contents on the site through the admin panel. 
***I've restricted the actions for the user that represents the dealer to the actions related to the car object. So, in the admin panel, the site's owner can only create, delete and update car objects***. 

---

#### Homepage

The site's homepage contain three main sections: 

1. Hero Section

![Hero Image](https://i.imgur.com/1urs2Ce.png)

2. Showcase Section 

![Showcase Image1](https://i.imgur.com/0EFc5Tw.png)


![Showcase Image2](https://i.imgur.com/ZWYmvpq.png)

This section contains cars chosen by the dealer. 
The car model contains the ***showcase*** field (a boolean field)and the dealer can choose cars that must be included in this section using the checkbox field in the admin panel's creation form. 

To retrieve the cars to show in this section I make an Axios get request to an endpoint that returns a list of all the car's adverts with ```showcase = True``` 

3. Footer

![Footer](https://i.imgur.com/3wV2mBR.png)

---

#### Store Page 

![Store Image](https://i.imgur.com/BB0sxpW.png)

#### Car Details Page

![Details Image1](https://i.imgur.com/3dQnf9R.png)


![Details Image2](https://i.imgur.com/YlVuwvE.png)

#### About Page 

![About Image](https://i.imgur.com/0iAZXZE.png)

---

#### Company Informations

I've created a database model to store informations about the company. 

```Python
class CompanyInfo(models.Model):
    address = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    idCode = models.CharField(max_length=100)

    def __str__(self):
        return 'company-informations'
```

When the site is launched I make a request to the following endpoint: 

```Python
class GetCompanyInfo(APIView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        object = CompanyInfo.objects.get(id=id)
        serializer = InfoSerializer(object)
        return Response(serializer.data)
```

and I store these informations on the frontend using Vuex: 

```JS
export default createStore({
    state:{
        address: '', 
        number: '', 
        email: '', 
        id: '', 
    }, 
    getters:{},
    mutations:{
        setItems(state, info){
            state.address = info.address, 
            state.number = info.number, 
            state.email = info.email, 
            state.id = info.id
        }
    },
    actions:{
        setItems({ commit }, info) {
            commit('setItems', info);
        }
    },
    modules:{},
})
```

_App.vue_:

```JS
export default {
  name: 'App',
  components: { Newsletter },
  methods: {
    ...mapActions(['setItems']),
    getInformations() {
      axios
        .get('api/company-info/1/')
        .then(response => {
          this.setItems({
            address: response.data.address,
            number: response.data.phoneNumber,
            id: response.data.idCode, 
            email: response.data.email
          });
        })
        .catch(error => {
          this.$router.push({name: 'error'})
        });
    },
  },
  mounted() {
    this.getInformations();
  }
}
```

In this way I can access these informations from all the components in my application.

This way, it is easier to update the informations because I only need to change the object stored in the database, instead of heaving to change each peace of information on every page of the website. 

---

### Preview

After cloning this repository you need to set up both Django and Vue 

1. ***Django***

Create a virtual environment with the ```python -m venv env_name``` Launch this environment and install all the projects dependencies: 

```bash
source env_name/bin/activate
pip install -m ./requirements.txt
```

Then run the django migrations: 

```bash
python manage.py makemigrations
python manage.py migrate
```

I've set up a dump data file called _data_dump.json_ Load those data in the database with the following command: 

```bash
python manage.py loaddata data_dump.json
```

To run the server 

```bash
python manage.py runserver
```

2. ***Vue***

To set up the Vue part you need to access the frontend repository and install all the Vue dependencies with the following commands: 

```bash
cd frontend
npm install
```

Run the server for the frontend

```bash
npm run serve
```


***Go to [server](http://localhost:8080) and the app is now running in development mode***