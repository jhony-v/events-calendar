<template>
  <div class="auth">
    <div class="auth-form">
        <auth-form-title></auth-form-title>
        <input-field label="Username or email" class="input" @oninput="username = $event"></input-field>
        <input-field label="Type your password" class="input" @oninput="password = $event"></input-field>
        <router-link class="auth-form__forword" to="/">Forworg password?</router-link>
        <div class="auth-form__button" tabindex="0" @keyup.enter="onAuthSignIn" @click="onAuthSignIn">Sign In</div>
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
    outline: none;
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
        color: var(--color-primary);
        font-size: 13px;
        @extend %auth-form-block;
    }
    &__button {
        color: var(--color-primary);
        font-size: 1.2em;
        padding: 10px;
        @extend %auth-form-block;
        border: 1px solid transparent;
        border-radius: 10px;
        transition: border-color .3s;
        &:focus {
            border-color: currentColor;
        }
    }
}
</style>
