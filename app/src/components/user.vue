<template>
<div>
    <div v-if="modal == 0">
        <div>
            <h1>Users</h1>
            <button class="btn btn-primary mb-2" @click="inputData = {name: ''};
            modal = 1">add</button>
        </div>

        <div class="form-inline mb-2">
            <label v-for="val in data" :key="val.id" class="form-check-label mr-3">
                <input type="radio" v-model="select" class="form-check-input "
                name="user" :value="val"><span>{{val.name}}</span>
            </label>

            <button class="btn btn-primary mr-2" @click="inputData = select; modal = 2">edit</button>
            <button class="btn btn-outline-primary" @click="deleteData(select.id)">remove</button>
        </div>
        
        <order v-if="select.id" class="p-5" :filter_id="select.id" :book_prop="book" :key="select.id"></order>
    </div>
    
    <!-- user edit menu -->
    <div v-else >
        <div class="form-group">
            <label for="user_name">Name</label>
            <input type="text" class="form-control mr-2" v-model="inputData.name">
        </div>

        <button class="btn btn-primary mr-2" v-if="modal == 1" @click="addData()">ok</button>
        <button class="btn btn-primary mr-2" v-if="modal == 2" @click="updateData(select.id)">ok</button>
        <button class="btn btn-outline-primary mr-2" @click="modal=0">cancel</button>
    </div>

</div>
</template>
<script>
import mixin from './mixins/scriptMixin';
import order from './order.vue';
import axios from 'axios';

export default{
    mixins: [mixin],
    mounted(){
        this.getBook();
    },
    data(){
        return {
            // data: [],
            select: '',
            // add: null,
            // edit: null,
            route: 'user',
            book: [],
        }
    },
    components:{
        order,
    },
    methods:{
        getBook(){
            axios.get(`/api/book/`).then(response=>{
                this.book = response.data;
            });
        }
    }
}
</script>