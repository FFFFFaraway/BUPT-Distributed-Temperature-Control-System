const api = 'http://127.0.0.1:5000/rooms/'

const axios = require('axios');

export default {
    state: {
        rooms: [],
        loading: false,
    },

    mutations: {
        update_id_room(state, id, room) {
            state.rooms.data[id] = room;
        },
        update_rooms(state, rooms) {
            state.rooms = rooms;
        },
        set_loading(state, loading) {
            state.loading = loading;
        }
    },

    actions: {
        getRooms({ commit }) {
            commit('set_loading', true);
            return axios.get(api)
                .then((rooms) => {
                    commit('update_rooms', rooms)
                    commit('set_loading', false)
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        checkIn({ commit, state, dispatch }, id) {
            commit('set_loading', true);
            return axios.post(api + 'checkIn', state.rooms.data[id])
                .then(function (response) {
                    commit('update_id_room', id, response);
                    commit('set_loading', false)
                    dispatch('getRooms');
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        checkOut({ commit, state, dispatch }, id) {
            commit('set_loading', true);
            return axios.post(api + 'checkOut', state.rooms.data[id])
                .then(function (response) {
                    commit('update_id_room', id, response);
                    commit('set_loading', false);
                    dispatch('getRooms');
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        flipPower({ commit, dispatch }, roomId) {
            commit('set_loading', true);
            return axios.post(api + 'flipPower', { id: roomId })
                .then((room) => {
                    commit('update_id_room', { id: roomId, room: room });
                    commit('set_loading', false);
                    dispatch('getRooms', null);
                })
        },
        temp_add({ commit, dispatch }, payload) {
            commit('set_loading', true);
            return axios.post(api + 'temp_add', payload)
                .then((room) => {
                    commit('update_id_room', { id: payload.id, room: room });
                    commit('set_loading', false);
                    dispatch('getRooms', null);
                })
        },
        set_speed({ commit, dispatch }, payload) {
            commit('set_loading', true);
            return axios.post(api + 'set_speed', payload)
                .then((room) => {
                    commit('update_id_room', { id: payload.id, room: room });
                    commit('set_loading', false);
                    dispatch('getRooms', null);
                })
        },
    },
    namespaced: true,
};
