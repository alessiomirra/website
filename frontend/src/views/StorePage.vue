<template>
    <div class="main">
        <Navbar />
        <div class="container mt-2 mb-5">
            <h3>Store</h3>
            <p class="text-muted">
                All cars we have in stock
            </p>
            <div v-if="cars.length">
                <div class="row">
                    <div class="col-lg-4 mb-3" v-for="car in cars">
                        <div class="card">
                            <div class="card-body">
                                <h5>{{ car.make }} {{ car.model }}</h5>
                                <p class="text-muted">
                                    {{ car.version }}
                                </p>
                                <div class="image">
                                    <img v-if="car.miniature" :src="car.miniature" alt="#">
                                    <div v-else class="no-image">
                                        <p>Images'll be available soon</p>
                                    </div>
                                </div>
                                <div class="details d-flex justify-content-around mt-3 mb-5">
                                    <span><i class="fa-solid fa-calendar-days"></i> {{ car.year }}</span>
                                    <span><i class="fa-solid fa-gas-pump"></i> {{ car.fuel }}</span>
                                    <span><i class="fa-solid fa-gear"></i> {{ car.gear }}</span>
                                </div>
                                <div class="card-bottom d-flex justify-content-between">
                                    <h4>€{{ car.price }}</h4>
                                    <router-link :to="{name:'car-details', params: {slug: car.slug}}" class="btn btn-primary">More Info</router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div v-if="next">
                <button class="btn btn-sm btn-outline-primary text-decoration-underline" @click="getCars">+ Load More</button>
            </div>

            <div v-if="loading" class="text-center">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'; 

import Navbar from '@/components/Navbar.vue';

export default{
    name: 'store-page', 
    components: {
        Navbar
    },
    data(){
        return{
            cars: [], 
            next: null, 
            loading: false, 
        }
    }, 
    methods:{
        async getCars(){
            this.loading = true; 
            let endpoint = 'api/cars/'; 
            if (this.next){
                endpoint = this.next; 
            }
            await axios 
                .get(endpoint)
                .then(response => {
                    this.cars.push(...response.data.results);

                    if (response.data.next){
                        this.next = response.data.next; 
                    } else {
                        this.next = null; 
                    }

                    this.loading = false; 
                })
                .catch(error => {
                    this.$router.push({
                        name: 'error'
                    })
                    console.log(error.response); 
                })
        }
    }, 
    mounted(){
        this.getCars(); 
        document.title = 'CarHub - Store Page'
    }
}
</script>

<style scoped>
.main{
    width: 100%;
    min-height: 100vh;
    opacity: 0; 
    animation: fadeInAnimation 0.5s ease-in forwards; 
}

.image{
    width: 100%;
    height: 200px;
}
.image img{
    width: 100%;
    height: 100%;
    object-fit: contain;
}
.no-image{
    width: 100%;
    height: 100%;
    background-color: #e5e5e5;
    display: flex;
    justify-content: center;
    align-items: center;
}
.card{
    min-height: 300px;
}


@keyframes fadeInAnimation {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
}
</style>