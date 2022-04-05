const app = Vue.createApp({
    //template: '<h2>I am the template</h2>,
    data(){
        return{
            name:"Thant Kyaw Swar Soe",
            icon : "<strong>panda</strong>",
            age:21,
            status:true,
            title : "My Paragraph",
            photo:"../level3/images/pic1.jpg",
            mark : 30,
            favfruits :['apple','papya','lime'],
            count:0,
            fname:"",
            ffname:"",
            ffage:"",
            ffgender:"",
            friends:[],
        }
    },
    methods:{
        greet(){
            alert(this.name)
        }
    },
    savefriends(){
        let friend={name:this.ffname,age:this.ffage,gender:this.ffgender}
        console.log(friend)
        this.friends.push(friend)
    },
})
//console.log(app)
app.mount("#app")
