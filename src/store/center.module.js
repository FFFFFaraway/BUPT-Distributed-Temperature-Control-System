const api = 'http://127.0.0.1:5000/center/'

const axios = require('axios');

export default {
    state: {
        power: false,
        state: 'Standby',
        mode: 'Cold',
        temp: 25,
        loading: false,
    },

    mutations: {
        set_center(state, center){
            state.power = center.data.power;
            state.state = center.data.state;
            state.mode = center.data.mode;
            state.temp = center.data.temp;
        },
        set_loading(state, loading) {
            state.loading = loading;
        },
    },

    actions: {
        getCenter({ commit }) {
            commit('set_loading', true);
            return axios.get(api)
                .then((center) => {
                    commit('set_center', center)
                    commit('set_loading', false)
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        flipPower({ commit }) {
            commit('set_loading', true);
            return axios.post(api + 'flipPower')
                .then((center) => {
                    commit('set_center', center)
                    commit('set_loading', false)
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        setMode({ commit }, mode) {
            commit('set_loading', true);
            return axios.post(api + 'setMode', {mode:mode})
                .then((center) => {
                    commit('set_center', center)
                    commit('set_loading', false)
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        temp_add({ commit }, offset) {
            commit('set_loading', true);
            return axios.post(api + 'temp_add', {offset:offset})
                .then((center) => {
                    commit('set_center', center)
                    commit('set_loading', false)
                })
                .catch((error) => {
                    console.error(error)
                })
        },
    },
    namespaced: true,
};
