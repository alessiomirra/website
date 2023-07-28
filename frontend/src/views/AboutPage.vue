<template>
    <div class="main">
        <Navbar />

        <div class="hero d-flex align-items-end">
            <div class="container p-3 hero-text">
                <div class="text">
                    <p>About us</p>
                    <h1 class="display-3">CarHub</h1>
                    <h1 class="display-5">Passion and Knowledge</h1>
                </div>
            </div>
        </div>

        <div class="container mt-3">
            <div class="row mb-3">
                <div class="col-lg-6">
                    <div class="text-center border rounded-5 p-3 info-text">
                        <p class="fs-5">
                            We are proud to offer a wide range of cars and services, including pre-delivery car inspection, warranty and assistance.
                        </p>
                    </div>
                </div>
                <div class="col-lg-6"></div>
            </div>
            <div class="row mb-3">
                <div class="col-lg-6"></div>
                <div class="col-lg-6">
                    <div class="text-center border rounded-5 p-3 info-text">
                        <p class="text-muted">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque imperdiet aliquet neque in fermentum. Vivamus arcu eros, suscipit at tincidunt eget, consectetur nec lectus. Mauris turpis erat, convallis vitae eros id, molestie faucibus arcu. Nunc magna massa, blandit at pharetra vel, tincidunt eu nulla. Donec sed dictum purus. Praesent scelerisque mi congue tincidunt rhoncus. Etiam eget rhoncus metus. Aliquam erat volutpat.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="container mb-5">
            <div class="image-container border">
                <img src="@/assets/images/car-park.jpeg" alt="#" loading="lazy">
            </div>
        </div>

        <div class="container mb-5">
            <div class="row justify-content-center">
                <div class="col-lg-12">
                    <div>
                        <h6 class="text-decoration-underline">Visit the store:</h6>
                        <p>{{ $store.state.address }}</p>
                        <p>tel: {{ $store.state.number }}</p>
                        <router-link :to="{name:'contact'}" class="btn btn-sm btn-primary">Contact</router-link>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
export default{
    name: 'AboutPage', 
    components: {Navbar}, 
    data(){
        return{

        }
    },
    mounted(){
        document.title = 'About Us'; 
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
.hero{
    height: 60vh;
    background-image: url('@/assets/images/park-2.jpeg'); 
    background-size:cover;
    background-repeat: no-repeat;
}
.hero-text{
    width: 100%;
}
.show{
    transform: translateX(0);
    opacity: 1;
}
.image-container{
    height: 400px;
}
.image-container img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.numbers{
    width: 40%;
    height: 100%;
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