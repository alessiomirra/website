<template>
    <div class="text-center">
        <p class="text-decoration-underline">Newsletter</p>
          <p>Join our newsletter to stay updated with the latest arrivals </p>
          <form @submit.prevent="subscribe">
            <div class="d-flex">
                <input type="email" class="form-control" placeholder="Email" v-model="email">
                <button type="submit" class="btn btn-primary ms-2">Subscribe</button>
            </div>
          </form>
        <small :class="[error ? 'text-danger':'text-success']">{{ message }}</small>
    </div>
</template>

<script>
import axios from 'axios'

export default({
    name: 'NewsletterComponent', 
    data(){
        return{
            email: '', 
            message: '', 
            error: false, 
        }
    }, 
    methods:{
        async subscribe(){
            this.message = ''; 
            if (this.email === ''){
                this.message = 'You must type a valid email!';
            } else {
                await axios 
                    .get(`newsletter/subscribe/${this.email}/`)
                    .then(response => {
                        if (response.data.type === 'error'){
                            this.message = response.data.message; 
                            this.email = ''; 
                            this.error = true;
                        } else {
                            this.message = response.data.message; 
                            this.email = ''; 
                            this.error = false; 
                        }
                    })
                    .catch(error => {
                        this.$router.push({
                            name: 'error'
                        })
                        this.error = true; 
                        this.email = ''; 
                        this.message = error.message; 
                    })
            }
        }
    }, 
})
</script>

<style scoped></style>