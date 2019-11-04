import Vue from 'vue';
//import 'bootstrap';
import axios from 'axios';


import user from './components/user.vue';
import book from './components/book.vue';
//import mixin from './components/mixins/scriptMixin';
// Vue.component('user', require('./components/user').default);
// Vue.component('book', require('./components/book').default);


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";


var app = new Vue({
    el: '#app',
    //mixins: [mixin],
    components:{
        user,
        book,
    }
})