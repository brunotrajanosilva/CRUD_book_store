<template>
<div>
    <div v-if="modal == 0">
        <div class="d-flex">
            <h3>livros: </h3>
            <button class="btn btn-primary ml-2 mb-2"
            @click="inputData = {name: '', pages: ''}; modal = 1">adicionar</button>
        </div>
        
        <ul class="grid-default">
            <li v-for="val in data" :key="val.id" class="grid-item">
                <h3>{{val.name}}</h3>
                <h3>número de páginas: {{val.pages}}</h3>
                <h3>preço: {{val.price}}</h3>
                <button class="btn btn-primary mr-2" @click="inputData = val;
                modal = 2">editar</button><button class="btn btn-outline-primary"
                @click="deleteData(val.id)">deletar</button>
            </li>
        </ul>
    </div>
    <div v-else class="d-flex">
        <input type="text" class="mr-2 form-control" v-model="inputData.name">
        <input type="number" class="mr-2 form-control" v-model="inputData.pages">
        <input type="number" class="mr-2 form-control" v-model="inputData.price" max="999.99" step=".01">
        <button class="mr-2 btn btn-primary" v-if="modal == 1" @click="addData()">OK</button>
        <button class="mr-2 btn btn-primary" v-if="modal == 2" @click="updateData(inputData.id)">OK</button>
        <button class="btn btn-outline-primary" @click="modal=0">cancelar</button>
    </div>
</div>
</template>
<script>
import mixin from './mixins/scriptMixin';

export default{
    mixins: [mixin],
    // mounted(){
    //     this.getData();
    // },
    data(){
        return {
            route: 'book',
        }
    },
    // methods:{
    //     change(id){
    //         let modal = this.modal;

    //         if(modal == 1){
    //             this.addData();

    //         }else if(modal == 2){
    //             this.updateData(id);

    //         }

    //         this.modal = 0;
    //     },
    //     getData(){
    //         axios.get(`/api/${this.route}/`).then(response=>{
    //             this.data = response.data;
    //         });
    //     },
    //     updateData(id){
    //         axios.patch(`/api/${this.route}/${id}/`, this.edit).then(response=>{
    //             this.getData();
    //             this.edit = null;
    //         });
    //     },
    //     addData(){
    //         axios.post(`/api/${this.route}/`, this.edit).then(response=>{
    //             this.getData();
    //             this.edit = null;
    //         });
    //     },
    //     deleteData(id){
    //         axios.delete(`/api/${this.route}/${id}/`).then(response=>{
    //             this.getData();
    //         });
    //     }
    // }
}
</script>