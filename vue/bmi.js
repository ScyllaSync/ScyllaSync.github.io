const app = Vue.createApp({
    data(){
       return{
        kilograms:"",
        centimeter:"",
        bmi:"",
       }
    },
    methods:{
        computeBMI(){
            this.bmi=this.kilograms/((this.centimeter/100)*(this.centimeter/100))
        }
    }
})
app.mount("#appforbmi")