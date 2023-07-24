<template>

    <div v-if="cars.length" class="row">
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
                        <router-link :to="{name:'car-details', params:{slug: car.slug}}" class="btn btn-primary">More Info</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'; 

export default{
    name: 'ShowcaseSection', 
    data(){
        return{
            cars: [], 
        }
    }, 
    methods:{
        getCars(){
            axios  
                .get('api/showcase/')
                .then(response => {
                    this.cars.push(...response.data); 
                })
                .catch(error => {
                    this.$router.push({
                        name: 'error'
                    })
                })
        }, 
    }, 
    mounted(){
        this.getCars(); 
    }
}
</script>

<style scoped>
.card{
    min-height: 300px;
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
</style>