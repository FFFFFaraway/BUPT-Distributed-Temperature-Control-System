const api = 'http://127.0.0.1:5000/form/';

const axios=require("axios");

export default{
	state:{
		loading:false,
		roomList:[],
		form:[],
		summary:[]
	},
	mutations:{
		flip_loading(state){
			state.loading=!state.loading;
		},
		set_loading(state,val){
			state.loading=val;
		},
		set_form(state,form){
			state.form=form;
		},
		set_roomList(state,n){
			state.roomList=n;
		},
		set_summary(state,s){
			state.summary=s;
		}
	},
	actions:{
		getForm({commit},data){
			commit("set_loading",true);
			return axios.post(api+'rep',data)
						.then(function(res){
							commit('set_loading',false);
							commit('set_form',res.data);
							var summary=[];
							var t=res.data;
							for(var i=0;i<t.length;i++){
								var flag=false;
								for(var j=0;j<summary.length;j++){
									if(summary[j].id==t[i].id){
										summary[j].On_Off_Times+=(t[i].type==1?1:0);
										summary[j].cost+=t[i].cost;
										flag=true;
										break;
									}
								}
								if(flag==false)
									summary.push({id:t[i].id,On_Off_Times:(t[i].type==1?1:0),cost:t[i].cost});
							}
							commit('set_summary',summary);
						})
						.catch((error)=>{console.log(error)});
		},
		getRoomList({commit}){
			return axios.get(api+'roomList')
						.then(
							function(rl){
								commit('set_roomList',rl.data);
							}
						)
						.catch((error)=>{console.log(error)});
		}
	},
	namespaced:true
}