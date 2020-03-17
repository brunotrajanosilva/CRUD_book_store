import Vue from 'vue';
import axios from 'axios';


import user from './components/user.vue';
import book from './components/book.vue';



axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";


var app = new Vue({
    el: '#app',
    components:{
        user,
        book,
    }
})