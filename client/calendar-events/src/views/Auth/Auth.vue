<template>
  <div class="auth">
    <div class="auth-form">
        <div class="auth-form__title--master auth-form__title">CALENDAR <i class="material-icons">emoji_events</i> EVENTS</div>
        <h3 class="auth-form__title">LOGIN</h3>
        <input-field label="Username or email" :style="{marginBottom:'2em'}" ></input-field>
        <input-field label="Type your password" :style="{marginBottom:'2em'}" type="password"></input-field>
        <router-link class="auth-form__forword" to="/">Forworg password?</router-link>
        <div class="auth-form__button">Sign In</div>
        <div class="auth-form__options">
            <div class="auth-form__google"><img src="https://image.flaticon.com/teams/slug/google.jpg" width="30px" />  Sign in with Google</div>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import InputField from "@/components/styled/InputField.vue";

@Component({
  components: {
    "input-field": InputField,
  },
})
export default class Auth extends Vue {}
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
    &__title {
        color: rgb(90,90,90);
        font-size: 1.2em;
        @extend %auth-form-block;
        &--master {
            margin-bottom: 3em;
            display: flex;
            align-items: center;
            justify-content: center;
            .material-icons {
                color: rgb(30, 190, 230);
                font-size: 2em;
            }
        }
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
    &__options {
        background: rgba(0,0,0,.03);
        padding: 2em;
        margin: -3em;
        margin-top: 2em;
        text-align: center;
        #{$self}__google {
            display: inline-flex;
            align-items: center;
            font-weight: bold;
            font-size: 14px;
            color: rgb(90,90,90);
            cursor: pointer;
        }
    }
}
</style>
