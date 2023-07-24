<template>
  <router-view/>
  <div class="footer">
    <div class="container p-2">

      <div class="footer-header text-center">
        <h4><i class="fa-sharp fa-solid fa-car-side"></i> CarHub</h4>
        <h5>Find,book and buy your new car.</h5>
        <hr>
      </div>

      <div class="row">
        <div class="col-md-3 mb-3 text-center">
          <p class="text-decoration-underline">About</p>
          <p><router-link :to="{name: 'contact'}" id="footer-link">Contact</router-link></p>
          <p><a href="#" id="footer-link">Informations</a></p>
          <p><a href="#" id="footer-link">Privacy Policy</a></p>
          <p><a href="#" id="footer-link">Cookies Policy</a></p>
        </div>
        <div class="col-md-3 mb-3 text-center">
          <p class="text-decoration-underline">Cars</p>
          <p><router-link href="#" id="footer-link" :to="{name: 'store-page'}">Car Store</router-link></p>
          <p><a href="#" id="footer-link">Warranty Conditions</a></p>
          <p><router-link :to="{name: 'unsubscribe'}" id="footer-link">Newsletter Unsubscribe</router-link></p>
        </div>
        <div class="col-md-6 mb-3">
          <Newsletter />
        </div>
      </div>

      <div class="infoes text-center">
        <div class="social-icons text-center mb-4">
          <span><i class="fa-brands fa-facebook fa-xl mx-4"></i></span>
          <span><i class="fa-brands fa-instagram fa-xl mx-4"></i></span>
          <span><i class="fa-brands fa-linkedin fa-xl mx-4"></i></span>
          <span><i class="fa-brands fa-tiktok fa-xl mx-4"></i></span>
        </div>
        <p>{{ $store.state.address }}</p>
        <p>{{ $store.state.email }}</p>
        <p>tel: <span class="text-decoration-underline">{{ $store.state.number }}</span></p>
        <p>ID: {{ $store.state.id }}</p>
        <div class="hr-with-word">
          <hr>
          <span class="text-center">@Copyright2023, <a href="#" class="text-decoration-underline text-primary">Alessio Mirra</a></span>
          <hr>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {mapActions} from 'vuex'; 
import Newsletter from './components/Newsletter.vue';
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
</script>

<style>
body{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
}

.footer{
  width: 100%;
  min-height: 400px;
  background-color: #023047;
  color: #ffffff;
}
#footer-link{
  color: white;
  text-decoration: none;
}
.hr-with-word {
  display: flex;
  align-items: center;
  width: 100%;
  margin: 10px 0;
  margin-top: 30px;
}
.hr-with-word hr {
    flex-grow: 1;
    margin: 0 10px;
    border: none;
    border-top: 1px solid white;
}
.hr-with-word span{
    width: 30%;
}

@media print{
  .footer{
    display: none;
  }
}
</style>
