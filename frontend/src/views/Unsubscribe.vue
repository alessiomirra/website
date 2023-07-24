<template>
    <div class="main">
        <Navbar />
        <div class="container text-center">
            <h4 class="mt-3 mb-3">Unsubscribe from Newletter</h4>

            <p class="text-muted mb-5">
                if you wish no longer to receive any email marketing messages from <span class="text-decoration-underline">CarHub</span>,
                 please confirm your email and click <span class="text-decoration-underline">Unsubscribe</span>
            </p>

            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-md-6">
                    <form class="form-control p-3" @submit.prevent="unsubscribe">
                        <div class="d-flex">
                            <input type="email" class="form-control" placeholder="Email" v-model="email">
                            <button type="submit" class="btn btn-primary ms-2">Unsubscribe</button>
                        </div>
                        <small :class="[error ? 'text-danger':'text-success']">{{ message }}</small>
                    </form>
                </div>
                <div class="col-md-3"></div>
            </div>

            <div class="mt-5 text-start">
                <div class="row">
                    <div class="col-md-4"></div>
                    <div class="col-md-4 border rounded-5 p-4">
                        <h5>Reason for unsubscribe</h5>
                        <p class="mb-5">(optional)</p>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                            <label class="form-check-label" for="flexRadioDefault1">
                                I'm changing my email address
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                            <label class="form-check-label" for="flexRadioDefault1">
                                The content isn't relevant
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                            <label class="form-check-label" for="flexRadioDefault1">
                                I get too many emails from you
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                            <label class="form-check-label" for="flexRadioDefault1">
                                Other 
                            </label>
                        </div>
                    </div>
                    <div class="col-md-4"></div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue';

export default{
    name: "Unsubscribe",
    components: {Navbar}, 
    data(){
        return{
            email: '', 
            message: '', 
            error: false, 
        }
    }, 
    methods: {
        async unsubscribe(){
            this.message = ''; 
            if (this.email === ''){
                this.message = 'You must type a valid email!';
            } else {
                await axios 
                    .get(`newsletter/unsubscribe/${this.email}/`)
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
                        this.error = true; 
                        this.email = '';
                        this.message = error.message;
                    })
            }
        }
    }, 
    mounted(){
        document.title = 'CarHub - Unsubscribe from newsletter'; 
    }
}
</script>

<style scoped>
.main{
    width: 100%;
    min-height: 100vh;
}

</style>