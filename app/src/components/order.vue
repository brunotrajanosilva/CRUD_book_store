<template>
<div>
    <div v-if="modal == 0">
        <div>
            <h1>Orders</h1>
            <button class="btn btn-primary mb-2"
            @click="inputData = {user: filter_id, book: []}; modal = 1">add</button>
        </div>
        <ul class="grid-default">
            <li v-for="val in orders" :key="val.id" class="grid-item">
                <h3 class="order-id">ID: {{val.order_id}}</h3>
                <h3>data: {{val.created_at}}</h3>
                <ul class="order-book">
                    <li class="badge badge-primary mr-1 mb-1" v-for="book in filterBooks(val.book)"
                    :key="book.id">{{book.name}}</li>
                </ul>
                <button class="btn btn-outline-primary" @click="deleteData(val.id)">remove</button>
            </li>
        </ul>
    </div>

    <!-- edit menu  -->
    <div v-else>
        <ul class="order-select-book">
            <div v-for="(val, index) in filterBooks(inputData.book)"
            :key="val.id" class="d-flex mb-2">
                <h3 class="mr-2">{{val.name}}</h3>
                <button class="btn btn-outline-primary" 
                @click="inputData.book.splice(index, 1)">remove</button>
            </div>
        </ul>

        <div class="form-inline">
            <select style="width:200px" name="" id="" class="form-control mr-2" width="100">
                <option v-for="book in selectBook" value="" :key="book.id"
                @click="inputData.book.push(book.id)">{{book.name}}</option>
            </select>
            <button class="btn btn-primary mr-2" @click="addData()">OK</button>
            <button class="btn btn-outline-primary" @click="modal=0">cancel</button>
        </div>
    </div>
</div>
</template>
<script>
import mixin from './mixins/scriptMixin';

export default {
    mixins: [mixin],
    props:['filter_id', 'book_prop'],
    data(){
        return {
            route: 'order',
        }
    },
    computed:{
        orders(){
            let data = this.data;
            let filter_id = this.filter_id;

            let result = data.filter(val=> val.user == filter_id);
            return result;
        },
        selectBook(){
            let book = this.book_prop;
            let inputData = this.inputData;

            let result = book.filter(x=>!inputData.book.some(y=> y == x.id));

            return result;
        },
    },
    methods:{
        filterBooks(arr){
            let book = this.book_prop;

            let result = book.filter(x=> arr.some(y=> y == x.id) );
            return result;
        },
    }
}
</script>