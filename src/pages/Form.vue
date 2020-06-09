<template>
	<div>
		<v-nav />
		<div v-if="login_adminEmail==''" class="container">
			<h1>Admin Page</h1>
			<p>Please sign in for more information</p>
		</div>
		<div v-else>
			<div>
				<b-card bg-variant="light">
					<b-form-group label-cols-lg="2" label="Form Infomation" label-size="lg" label-class="font-weight-bold pt-0" class="mb-0">
						<b-form-group label-cols-sm="2" label="Starting Date:" label-align-sm="left" label-for="sd">
							<b-form-datepicker id="sd" v-model="sd" class="mb-2"></b-form-datepicker>
						</b-form-group>
						<b-form-group label-cols-sm="2" label="Ending Date:" label-align-sm="left" label-for="ed">
							<b-form-datepicker id="ed" v-model="ed" class="mb-2"></b-form-datepicker>
						</b-form-group>
						<b-form-group label-cols-sm="2" label="Starting Room:" label-align-sm="left" label-for="sr">
							<b-form-select id='sr' v-model="sr" :options="roomList"></b-form-select>
						</b-form-group>
						<b-form-group label-cols-sm="2" label="Ending Room:" label-align-sm="left" label-for="er">
							<b-form-select id='er' v-model="er" :options="roomList"></b-form-select>
						</b-form-group>
						<b-button variant="outline-success" size="lg" @click="gf()">Submit</b-button>
					</b-form-group>
				</b-card>
				<b-overlay :show='loading'>
					<b-form-group label-cols-sm="2" label="Summary:" label-for="summary">
						<b-table striped hover :items="summary" id="summary"> </b-table>
					</b-form-group>
					<b-form-group label-cols-sm="2" label="Details:" label-for="detail">
						<b-table striped hover :items="form" id="detail"></b-table>
					</b-form-group>
				</b-overlay>
			</div>
		</div>
	</div>
</template>

<script>
	import VNav from "../components/VNav.vue";
	import Vuex from "vuex";

	const mapState = Vuex.mapState;
	const mapActions = Vuex.mapActions;

	export default {
		data() {
			return {
				sd: "",
				ed: "",
				sr: 0,
				er: 0,
			};
		},
		computed: {
			...mapState("auth", ["login_adminEmail"]),
			...mapState("form", ["loading", "roomList", "form", "summary"])
		},
		methods: {
			...mapActions("form", ["getForm", "getRoomList"]),
			gf: function() {
				var data = {
					sd: this.sd,
					ed: this.ed,
					sr: this.sr,
					er: this.er
				};
				this.getForm(data);
			}
		},
		components: {
			VNav
		},
		created() {
			this.getRoomList();
		}
	};
</script>
