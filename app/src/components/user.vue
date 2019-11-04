<template>
<div>
    <div v-if="modal == 0">
        <div class="d-flex">
            <h3>usuário: </h3>
            <button class="btn btn-primary ml-2 mb-2" @click="inputData = {name: ''};
            modal = 1">adicionar</button>
        </div>

        <div class="d-flex mb-2">
            <select name="" id="" v-model="select" class="form-control mr-2">
                <option v-for="val in data" :value="val" :key="val.id">{{val.name}}</option>
            </select>
            <button class="btn btn-primary mr-2" @click="inputData = select; modal = 2">editar</button>
            <button class="btn btn-outline-primary" @click="deleteData(select.id)">deletar</button>
        </div>
        
        <order v-if="select.id" class="p-5" :filter_id="select.id" :book_prop="book"></order>
    </div>
    
    <div v-else class="d-flex">
        <input type="text" class="mr-2" v-model="inputData.name">
        <button class="btn btn-primary mr-2" v-if="modal == 1" @click="addData()">ok</button>
        <button class="btn btn-primary mr-2" v-if="modal == 2" @click="updateData(select.id)">ok</button>
        <button class="btn btn-outline-primary mr-2" @click="modal=0">cancelar</button>
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
        this.getData();
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