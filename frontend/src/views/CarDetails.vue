<template>
    <div class="main">
        <Navbar />

        <div class="container mt-4" v-if="car">

            <div class="row">
                <div class="col-lg-8 box mb-3">
                    <div class="image-box">
                        <img v-if="car.miniature" :src="car.miniature" alt="#" class="rounded" loading="lazy">
                        <div v-else class="no-image">
                            <p>Images'll be available soon</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 border box rounded-3 mb-3 p-3">
                    <h4>{{ car.make }} {{ car.model }}</h4>
                    <h6 class="text-muted">{{ car.version }}</h6>
                    <div class="d-flex justify-content-between">
                        <span class="text-decoration-underline">(+39)333 128 1099</span>
                        <span>
                            <a href="#"><i class="fa-solid fa-share"></i></a> <a href="#" @click="print"><i class="fa-solid fa-print"></i></a>
                        </span>
                    </div>
                    <hr>
                    <div class="d-flex justify-content-between price-box">
                        <p>Price (VAT included):</p>
                        <p>€{{ car.price }}</p>
                    </div>
                    <hr>
                    <div>
                        <span class="me-2" id="small">{{ car.year }}</span>
                        <span class="me-2" id="small">{{ car.gear }}</span>
                        <span class="me-2" id="small">{{ car.fuel }}</span>
                        <span class="me-2" id="small">{{ car.mileage }} km</span>
                        <p class="text-muted"><i class="fa-solid fa-check"></i> 12 months warranty</p>
                    </div>
                    <hr>
                    <div class="d-flex financing">
                        <div>
                            <h6 class="text-decoration-underline">Financing</h6>
                        </div>
                        <div class="text-end">
                            <p>It is possible to buy this car by financing it. <span class="text-decoration-underline">More information</span></p>
                        </div>
                    </div>
                    <hr>
                    <div class="d-flex justify-content-around mt-5">
                        <button class="btn btn-info text-decoration-underline"><i class="fa-solid fa-phone-volume fa-l"></i>{{ $store.state.number }}</button>
                        <router-link :to="{name: 'contact'}" class="btn btn-primary">Contact</router-link>
                    </div>
                </div>
            </div>

            <div class="informations mb-3 border rounded-2 p-3">
                <h5 class="text-center mb-5 text-decoration-underline">SUMMARY OF THE FEATURES OF THE USED CAR</h5>
                <div class="row">
                    <div class="col-md-6 border-end text-center">
                        <p><span class="text-bold"><strong>Mileage:</strong></span> {{ car.mileage }} km</p>
                        <p><span class="text-bold"><strong>Gear:</strong></span> {{ car.gear }}</p>
                        <p><span class="text-bold"><strong>Warranty:</strong></span> 12 months warranty</p>
                        <p><span class="text-bold"><strong>Year:</strong></span> {{ car.year }}</p>
                    </div>
                    <div class="col-md-6 text-center">
                        <p><span class="text-bold"><strong>Fuel:</strong></span> {{ car.fuel }}</p>
                        <p><span class="text-bold"><strong>Power:</strong></span> {{ car.power }} kW</p>
                    </div>
                </div>
                <!-- Optionals -->
                <h6 class="text-center text-decoration-underline mt-3">OPTIONALS</h6>
                <div v-if="car.optionals && car.optionals.length" class="text-center">
                    <span>{{ car.optionals }}</span>
                </div>
                <div v-else class="text-center">
                    <p class="text-muted">No infoes about optionals for this car</p>
                </div>
                <!-- Description -->
                <h6 class="text-center text-decoration-underline mt-3">DESCRIPTION</h6>
                <div v-if="car.description" class="text-center">
                    <p>{{ car.description }}</p>
                </div>
                <div v-else class="text-center">
                    <p class="text-muted">No description available for this car</p>
                </div>
            </div>

        </div>
        

    </div>

</template>

<script>
import axios from 'axios';
import Navbar from '@/components/Navbar.vue';

export default{
    name: 'CarDetails', 
    components: {
        Navbar
    }, 
    data(){
        return{
            car: '', 
        }
    }, 
    methods:{
        async getCar(){
            const slug = this.$route.params.slug; 
            await axios 
                .get(`api/cars/${slug}/`)
                .then(response => {
                    this.car = response.data; 
                    document.title = `CarHub - ${this.car.make} ${this.car.model}`; 
                })
                .catch(error => {
                    this.$router.push({
                        name: 'error'
                    })
                    console.log(error.response);
                })
        }, 
        print(){
            window.print(); 
        }
    }, 
    mounted(){
        this.getCar();
    },
}

</script>

<style scoped>
.main{
    width: 100%;
    min-height: 100vh;
    opacity: 0; 
    animation: fadeInAnimation 0.5s ease-in forwards; 
}

.box{
    height: 500px;
}
.image-box{
    width: 98%;
    height: 100%;
}
.image-box img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.no-image{
    width: 100%;
    height: 100%;
    background-color: #e5e5e5;
    display: flex;
    justify-content: center;
    align-items: center;
}
.price-box{
    color: #4361ee;
}
#small{
    border: 1px solid black;
    border-radius: 5px;
    padding: 2px;
    background-color: grey;
    color: white;
}
.financing{
    cursor: pointer;
    color: #4cc9f0;
}
.informations{
    width: 100%;
    min-height: 200px;
}

@keyframes fadeInAnimation {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
}

@media (max-width: 800px){
    .image-box img{
        width: 100%;
        height: 100%;
        object-fit: contain;
    }    
}

</style>