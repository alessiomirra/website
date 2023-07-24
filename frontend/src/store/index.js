import { createStore } from 'vuex'; 

export default createStore({
    state:{
        address: '', 
        number: '', 
        email: '', 
        id: '', 
    }, 
    getters:{},
    mutations:{
        setItems(state, info){
            state.address = info.address, 
            state.number = info.number, 
            state.email = info.email, 
            state.id = info.id
        }
    },
    actions:{
        setItems({ commit }, info) {
            commit('setItems', info);
        }
    },
    modules:{},
})