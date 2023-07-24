<template>
    <div class="main bg-dark bg-opacity-75">

        <div class="navbar navbar-expand-lg bg-transparent">
            <div class="container">
                <router-link class="navbar-brand" :to="{name: 'home'}"><i class="fa-sharp fa-solid fa-car-side fa-xxl"></i> CarHub</router-link>
            </div>
        </div>

        <div class="warning">
            <div class="text-center text-light">
                <h1>Error</h1>
                <h3>Something went wrong</h3>
                <h6>Try going back to the <router-link :to="{name: 'home'}">homepage</router-link>. We are working to fix everything</h6>
                <p>We are sorry for the inconvenience</p>
            </div>
        </div>

    </div>
</template>

<script>
export default{
    name: 'ErrorPage', 
    data(){
        return{

        }
    }, 
    mounted(){
        document.title = 'CarHub - Error'; 
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
.navbar-brand{
    color: #ffffff;
}
.navbar-brand:hover{
    color: #ffffff;
}
.navbar-brand:active{
    color: #ffffff;
}
.warning{
    min-height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
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