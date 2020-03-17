<template>
<div>
    <div v-if="modal == 0">
        <div>
            <h1>Books</h1>
            <button class="btn btn-primary mb-2"
            @click="inputData = {name: '', pages: ''}; modal = 1">add</button>
        </div>
        
        <!-- books grid -->
        <ul class="grid-default">
            <li v-for="val in data" :key="val.id" class="grid-item">
                <h3>{{val.name}}</h3>
                <h3>Author: {{val.author}}</h3>
                <h3>Price: {{val.price}}</h3>
                <button class="btn btn-primary mr-2" @click="inputData = val;
                modal = 2">edit</button><button class="btn btn-outline-primary"
                @click="deleteData(val.id)">remove</button>
            </li>
        </ul>
    </div>

    <!-- edit menu -->
    <div v-else class="form">
        <div class="form-group">
            <label for="book_name">Name</label>
            <input type="text" id="book_name" class="mr-2 form-control" v-model="inputData.name">
        </div>

        <div class="form-group">
            <label for="book_author">Author</label>
            <input type="text" class="mr-2 form-control" id="book_author" v-model="inputData.author">
        </div>

        <div class="form-group">
            <label for="book_price">Price</label>
            <input type="number" class="mr-2 form-control" id="book_price" v-model="inputData.price"
            max="999.99" step=".01">
        </div>

        <button class="mr-2 btn btn-primary" v-if="modal == 1" @click="addData()">OK</button>
        <button class="mr-2 btn btn-primary" v-if="modal == 2" @click="updateData(inputData.id)">OK</button>
        <button class="btn btn-outline-primary" @click="modal=0">cancel</button>
    </div>
</div>
</template>
<script>
import mixin from './mixins/scriptMixin';

export default{
    mixins: [mixin],
    data(){
        return {
            route: 'book',
        }
    },
}
</script>