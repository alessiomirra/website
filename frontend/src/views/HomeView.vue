<template>

  <div class="main">

    <div class="top">
    
      <div class="navbar navbar-expand-lg bg-transparent">
        <div class="container">
          <a class="navbar-brand" href="#"><i class="fa-sharp fa-solid fa-car-side fa-xxl"></i> CarHub</a>
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
      </div>

      <div class="center container d-flex justify-content-between mt-5">
        <div class="left pt-5">
          <h2>Welcome to CarHub!</h2>
          <h4>Find, book and buy your new car - <br>quick and super easy</h4>
          <p class="text-muted">Choose your new car and come to our store to see and try it!</p>
          <div class="d-flex mt-5 buttons">
            <router-link href="#" class="btn btn-primary" :to="{name: 'store-page'}">Store Page</router-link>
            <a href="#showcase-section" class="btn btn-light ms-2">Showcase</a>
          </div>
        </div>
        <div class="right">
          <img src="@/assets/images/heroCar.png" alt="#" loading="lazy">
        </div>
      </div>

    

    <div class="container text-center">
      <div class="row cards-pic justify-content-center">
        <div class="col-lg-4 mb-3">
          <div class="pic p-3">
            <div class="head">
              <i class="fa-sharp fa-solid fa-car-side fa-2xl"></i>
            </div>
            <div class="body mt-2">
              <h5>Find your new car</h5>
              <p class="text-muted">Find your new car among the many choices on our site</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 mb-3">
          <div class="pic p-3">
            <div class="head">
              <i class="fa-solid fa-building fa-2xl"></i>
            </div>
            <div class="body mt-2">
              <h5>Come to see the car</h5>
              <p class="text-muted">Contact us and come to see cars in our physical store</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 mb-3">
          <div class="pic p-3">
            <div class="head">
              <i class="fa-solid fa-file fa-2xl"></i>
            </div>
            <div class="body mt-2">
              <h5>Warranty</h5>
              <p class="text-muted">When you buy one of our cars you have a one year warranty</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    </div>

  </div>

  <div class="container">
    <hr>
  </div>

  <div class="showcase-section mb-4" id="showcase-section">

    <div class="container">
      <h3>Showcase Section</h3>
      <p class="text-muted">
        These are our best cars. For more cars visit our <router-link :to="{name: 'store-page'}">store</router-link>!
      </p>
      <div>
        <ShowcaseSection /> 
      </div>
    </div>

  </div>

</template>

<script>
// @ is an alias to /src
import ShowcaseSection from '@/components/showcase.vue';
export default {
  name: 'HomeView',
  components: {
    ShowcaseSection, 
  }, 
  mounted(){
    document.title = 'CarHub'; 
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
  color: #4361ee;
}
.navbar-brand:hover{
  color: #4361ee;
}
.navbar-brand:active{
  color: #4361ee;
}
.left{
  width: 50%;
  height: 400px;
}
.left h4{
  font-weight:400;
}
.right{
  width: 50%;
  height: 400px;
}
.right img{
  position: absolute;
  top: -5%;
}
.head i{
  color: #4361ee;
}
.cards-pic{
  width: 100%;
}
.pic{
  border: 0.5px solid grey;
  border-radius: 30px;
  width: 80%;
  min-height: 150px;
}



.showcase-section{
  width: 100%;
  min-height: 100vh;
}

@keyframes fadeInAnimation {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
}

@media (max-width: 1300px){
  .left{
    width: 100%;
    text-align: center;
  }
  .buttons{
    display: flex;
    justify-content: center;
  }
  .right{
    display: none;
  }
  .cards-pic{
    margin-left: 6%; 
  }
}
</style>
