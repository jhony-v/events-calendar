<template>
  <div class="auth">
    <div class="auth-form">
        <auth-form-title></auth-form-title>
        <input-field label="Username or email" class="input" @oninput="username = $event"></input-field>
        <input-field label="Type your password" class="input" @oninput="password = $event"></input-field>
        <router-link class="auth-form__forword" to="/">Forworg password?</router-link>
        <div class="auth-form__button" @click="onAuthSignIn">Sign In</div>
        <auth-other-options></auth-other-options>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { State, Action } from "vuex-class"; 
import InputField from "@/components/styled/InputField.vue";
import AuthOtherOptionsAuthVue from './AuthOtherOptionsAuth.vue';
import AuthFormTitleVue from './AuthFormTitle.vue';
import { TypesStore } from "@/store/@types"

@Component({
  components: {
    "input-field": InputField,
    "auth-other-options" : AuthOtherOptionsAuthVue,
    "auth-form-title" : AuthFormTitleVue
  },
})
export default class Auth extends Vue {
    private username !: string;
    private password !: string;

    @Action("authSignIn",{namespace:"auth"}) authSignIn !: (e : TypesStore.AuthLoginVerifiy) => void;
    private onAuthSignIn() : void {
        this.authSignIn({username:this.username,password:this.password});
    }
}
</script>

<style lang="scss" scoped>
%auth-form-block {
    text-align: center;
    display: block;
    font-weight: bold;
    margin-bottom: 2em;
}

.auth {
    width: 100%;
    height: 100vh;
    display: flex;
}
.auth-form {
    $self : &;
    box-shadow: 0 10px 20px rgba(0,0,0,.1);
    border-radius: 10px;
    padding: 3em;
    margin: auto;
    width: 420px;
    .input {
        margin-bottom: 2em;
    }
    &__forword {
        color: rgb(30, 190, 230);
        font-size: 13px;
        @extend %auth-form-block;
    }
    &__button {
        color: rgb(30, 190, 230);
        font-size: 1.2em;
        @extend %auth-form-block;
    }
}
</style>
