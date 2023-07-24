<template>
    <div class="main">
        <Navbar />
        <div class="container">

            <div class="header text-center mt-2 mb-4">
                <h4>Contact</h4>
                <p class="text-muted">Any question or remarks? Just write us a message!</p>
            </div>

            <div class="row">

                <div class="col-lg-4 box info">
                    <div>
                        <h5>Contact Informations</h5>
                        <p id="thin-text">Say something to start a live chat!</p>
                    </div>
                    <div class="info-center">
                        <p><i class="fa-solid fa-phone-volume fa-l"></i><span class="text-decoration-underline ms-3">{{ $store.state.number }}</span></p>
                        <p><i class="fa-solid fa-envelope"></i><span class="ms-3">{{ $store.state.email }}</span></p>
                        <p><i class="fa-solid fa-location-dot"></i><span class="ms-3">{{ $store.state.address }}</span></p>
                    </div>
                    <div class="icons">
                        <span><a href="#"><i class="fa-brands fa-facebook fa-xl"></i></a></span>
                        <span><a href="#"><i class="fa-brands fa-instagram fa-xl ms-4"></i></a></span>
                        <span><a href="#"><i class="fa-brands fa-linkedin fa-xl ms-4"></i></a></span>
                        <span><a href="#"><i class="fa-brands fa-tiktok fa-xl ms-4"></i></a></span>
                    </div>
                </div>

                <div class="col-lg-8 box form-box">
                    <form @submit.prevent="submitForm" id="contact-form">
                        <div v-if="errors.length" class="alert alert-danger text-center" role="alert">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                        <div v-if="success" class="alert alert-success text-center" role="alert">
                            <p>Your message has been sent successfully!</p>
                        </div>
                        <div class="row">
                            <div class="col-lg-6 mb-3">
                                <label for="first-name" class="form-label">First Name</label>
                                <input type="text" class="form-control" :class="{error:firstNameError}" name="first-name" id="first-name" v-model="firstName"> 
                                <small v-if="firstNameError" class="text-danger">You must type your first name</small>
                            </div>
                            <div class="col-lg-6 mb-3">
                                <label for="last-name" class="form-label">Last Name</label>
                                <input type="text" class="form-control" :class="{error:lastNameError}" name="last-name" id="last-name" v-model="lastName"> 
                                <small v-if="lastNameError" class="text-danger">You must type your last name</small>
                            </div>
                            <div class="col-lg-6 mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control" :class="{error:emailError}" name="email" id="email" v-model="email"> 
                                <small v-if="emailError" class="text-danger">You must type your email</small>
                            </div>
                            <div class="col-lg-6 mb-3">
                                <label for="phone-number" class="form-label">Phone Number</label>
                                <input type="text" class="form-control" :class="{error:phoneNumberError}" name="phone-number" id="phone-number" v-model="phoneNumber"> 
                                <small v-if="phoneNumberError" class="text-danger">You must type your phone number</small>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-12">
                                <h6>Subject</h6>
                                <select name="subject" id="subject" class="form-select" :class="{error:subjectError}" v-model="subject">
                                    <option value=""></option>
                                    <option>Car Info</option>
                                    <option>General Question</option>
                                    <option>Remark</option>
                                    <option>Company Info</option>
                                </select>
                                <small v-if="subjectError" class="text-danger">You must select a subject for the message</small>
                            </div>
                        </div>
                        <div class="row mt-3 mb-3" v-if="changeVisibility">
                            <div class="col-12">
                                <h6>Select Car</h6>
                                <select name="car" id="car" class="form-select" v-model="car">
                                    <option value=""></option>
                                    <option v-for="car in cars" :key="car">{{ car }}</option>
                                    <option>Other</option>
                                </select>
                            </div>
                        </div>
                        <div class="row mt-3">
                            <div class="col-12">
                                <label for="message" class="form-label">Message</label>
                                <textarea name="message" id="message" cols="30" rows="3" class="form-control" :class="{error:messageError}" placeholder="Message" v-model="message"></textarea>
                                <small v-if="messageError" class="text-danger">You must type a message</small>
                            </div>
                        </div>
                        <div class=" d-flex justify-content-end mt-5">
                            <button type="submit" class="btn btn-dark submit-button">
                                <span v-if="isLoading" class="spinner-border text-light" role="status">
                                    <span class="visually-hidden">Loading...</span>
                                </span>
                                <span v-else>
                                    Send Message 
                                </span>
                            </button>
                        </div>
                    </form>

                </div>

            </div>

        </div>

    </div>
</template>

<script>
import axios from 'axios';
import Navbar from '@/components/Navbar.vue';

export default{
    name: 'ContactPage',
    components: {Navbar}, 
    computed: {
        changeVisibility(){
            if (this.subject === 'Car Info'){
                return true;  
            }
            return false; 
        }
    }, 
    data(){
        return{
            firstName: '',
            firstNameError: false, 
            lastName: '', 
            lastNameError: false, 
            email: '', 
            emailError: false, 
            phoneNumber: '', 
            phoneNumberError: false,
            subject: '', 
            subjectError: false, 
            message: '', 
            messageError: false, 
            errors: [], 
            car: 'None', 
            cars: [], 
            isLoading: false, 
            success: false, 
            selectCar: false, 
        }
    }, 
    methods:{
        submitForm(){
            this.isLoading = true; 
            this.errors = []; 
            this.firstNameError = false;
            this.lastNameError = false;
            this.emailError = false;
            this.phoneNumberError = false;
            this.subjectError = false;
            this.messageError = false;

            if (this.firstName === ''){
                this.firstNameError = true; 
            };
            if(this.lastName === ''){
                this.lastNameError = true; 
            }; 
            if(this.email === ''){
                this.emailError = true; 
            }; 
            if(this.phoneNumber === ''){
                this.phoneNumberError = true; 
            }; 
            if(this.subject === ''){
                this.subjectError = true; 
            };
            if(this.message === ''){
                this.messageError = true; 
            }; 

            if (!this.firstNameError && !this.lastNameError && !this.emailError && !this.phoneNumberError && !this.subjectError && !this.messageError && !this.errors.length){
                this.isLoading = true; 
                let formdata = {
                    firstName: this.firstName, 
                    lastName: this.lastName,
                    email: this.email, 
                    phoneNumber: this.phoneNumber, 
                    subject: this.subject, 
                    message: this.message,
                    car: this.car  
                }
                axios 
                    .post('/api/contact/', formdata)
                    .then(response => {
                        this.success = true; 
                        this.firstName = ''; 
                        this.lastName = ''; 
                        this.email = ''; 
                        this.phoneNumber = ''; 
                        this.subject = ''; 
                        this.message = ''; 
                    })
                    .catch(error => {
                        this.errors.push(error.response); 
                    })
            }

            this.isLoading = false; 
        }, 
        getAvailable(){
            axios 
                .get('/api/available/')
                .then(response => {
                    this.cars.push(...response.data); 
                })
                .catch(error => {
                    this.errors.push(error.response); 
                })
        },
    }, 
    mounted(){
        document.title = 'Contact Us'
        this.getAvailable(); 
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
    height: 520px;
    overflow-y: scroll;
}
.info{
    background-color: #023047;
    color: white;
    padding: 20px;
    border-radius: 30px;
}
#thin-text{
    font-weight: 100;
}
.icons a{
    color: white;
}
.info-center{
    margin-top: 30%;
}
.icons{
    margin-top: 40%;
}
.form-box{
    padding: 20px;
}
.form-control{
    border: none;
    border-bottom: 0.5px solid grey;
}
.form-control:focus{
    box-shadow: none;
    border-bottom: 1.5px solid black;
}
.form-select{
    border: none;
    border-bottom: 0.5px solid grey;
}
.form-select:focus{
    box-shadow: none;
    border-bottom: 1.5px solid black;
}
.error{
    border-bottom: 1.5px solid red; 
}
.submit-button{
    width: 200px;
    height: 50px;
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
    .info{
        text-align: center;
    }
    .info-center{
        margin-top: 10%;
    }
    .icons{
        margin-top: 20%;
    }
}
</style>