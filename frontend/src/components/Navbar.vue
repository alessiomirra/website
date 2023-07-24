<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <router-link class="navbar-brand" :to="{name: 'home'}"><i class="fa-sharp fa-solid fa-car-side fa-xxl"></i> CarHub</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page" :to="{name: 'store-page'}">Store Page</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page" :to="{name: 'about-page'}">About</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>    
</template>

<script>
export default{
    name: 'Navbar', 
}
</script>

<style scoped>
@media print{
    .navbar{
        display: none
    }
}
</style>