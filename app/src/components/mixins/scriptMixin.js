import axios from 'axios';

export default{
    mounted(){
        this.getData();
    },
    data(){
        return {
            data: [],
            inputData: null,
            modal: 0,
        }
    },
    methods:{
        getData(){
            axios.get(`/api/${this.route}/`).then(response=>{
                this.data = response.data;
            });
        },
        updateData(id){
            axios.patch(`/api/${this.route}/${id}/`, this.inputData).then(response=>{
                this.getData();
                this.inputData = null;
                this.modal = 0;
            });
        },
        addData(){
            axios.post(`/api/${this.route}/`, this.inputData).then(response=>{
                this.getData();
                this.inputData = null;
                this.modal = 0;
            });
        },
        deleteData(id){
            axios.delete(`/api/${this.route}/${id}/`).then(response=>{
                this.getData();
            });
        }
    }
};