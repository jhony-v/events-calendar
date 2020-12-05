<template>
  <div class="auth">
    <div class="auth-form">
        <auth-form-title></auth-form-title>
        <input-field label="Type your email" class="input" @oninput="username = $event"></input-field>
        <input-field type="password" label="Type your password" class="input" @oninput="password = $event"></input-field>
        <router-link class="auth-form__forword" to="/">Forworg password?</router-link>
        <div class="auth-form__button" tabindex="0" @keyup.enter="onAuthSignIn" @click="onAuthSignIn">Sign In</div>
        <auth-other-options-auth></auth-other-options-auth>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import { State, Action } from "vuex-class"; 
import InputField from "@/components/Packages/FormControls/InputField.vue";
import AuthOtherOptionsAuth from './AuthOtherOptionsAuth.vue';
import AuthFormTitle from './AuthFormTitle.vue';
import { UserNamespace } from '@/infraestructure/entities';

@Component({
    components: {
    InputField,
    AuthOtherOptionsAuth,
    AuthFormTitle,
  },
})
export default class Auth extends Vue {
    private email !: string;
    private password !: string;
    @Action("authSignIn",{namespace:"auth"}) authSignIn !: (e : UserNamespace.UserAuth) => void;
    private onAuthSignIn() : void {
        this.authSignIn({email:this.email,password:this.password});
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
    box-shadow: 0 10px 20px var(--color-border-neutral);
    background-color: var(--color-layout-primary);
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
