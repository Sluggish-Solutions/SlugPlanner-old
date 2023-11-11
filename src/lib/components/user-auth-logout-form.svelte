<script lang="ts">
  // import { Icons } from "$components/docs";
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import { Label } from "$lib/components/ui/label";
  import { signUpUser, logInUser} from "$lib/backend/auth";
  import type {SignUpResult} from "$lib/backend/auth"
  import { cn } from "$lib/utils";
  import { stringify } from "postcss";
  import * as Alert from "$lib/components/ui/alert";
  import {redirect} from '@sveltejs/kit'
  import { goto } from "$app/navigation";
  import Header from "../../routes/Header.svelte";

  let className: string | undefined | null = undefined;
  export { className as class };

  let isLoading = false;


    // Perform any necessary form validation or other actions before calling signUpUser
  

  // function signUp() {
  //  // Prevent the default form submission behavior
  //   // Your signUp logic here
  //   console.log("hi wtf")
  // }
</script>

<div class={cn("grid gap-6", className)} {...$$restProps}>

  <div class="relative">
    <div class="absolute inset-0 flex items-center">
      <span class="w-full border-t" />
    </div>
    <div class="relative flex justify-center text-s ">

      <span class="bg-background px-2 text-muted-foreground">
        If you were signed out by accident
        
      </span>

    </div>
  </div>
  <a href="/login" class="grid gap-1 ">
      <Button variant="outline"  type="button" disabled={isLoading}>
    {#if isLoading}
      <!-- <Icons.spinner class="mr-2 h-4 w-4 animate-spin" /> -->
    {:else}
      <!-- <Icons.git Hub class="mr-2 h-4 w-4" /> -->
    {/if}
    {" "}
    Log Back In Here
  </Button>
  </a>
  
</div>
