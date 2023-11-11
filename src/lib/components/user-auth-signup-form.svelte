<script lang="ts">
  // import { Icons } from "$components/docs";
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import { Label } from "$lib/components/ui/label";
  import { signUpUser} from "$lib/backend/auth";
  import type {SignUpResult} from "$lib/backend/auth"
  import { cn } from "$lib/utils";
  import { stringify } from "postcss";
  import * as Alert from "$lib/components/ui/alert";
  import {redirect} from '@sveltejs/kit'
  import { goto } from "$app/navigation";
 

  let className: string | undefined | null = undefined;
  export { className as class };

  let isLoading = false;

  let email: string;
  let password: string;
  let password2: string;
  let show_password_alert: boolean = false
	let show_error_alert: boolean = false
	let error_alert_text: string
	let error_alert_code: number
  const signUp = async (event: Event) => {
    event.preventDefault();

    //check if passwords match
	let password_check:boolean = password === password2


	if (password_check){
		show_password_alert = false
		try {
			let status:SignUpResult = await signUpUser(email, password);
			
			console.log(status)

			if(status.error !== null){
				show_error_alert = true
				error_alert_text = status.error.message
				error_alert_code = status.error.status
			}
			
		if (status?.data.user.aud === "authenticated"){
			goto("/select_prereqs")
		}


		} catch (error) {
			// prompt them to try again later? something went wrong?
			console.error("Sign up failed:", error)
		}


	} else {
		show_password_alert=true
	}
    // Perform any necessary form validation or other actions before calling signUpUser
  };

  // function signUp() {
  //  // Prevent the default form submission behavior
  //   // Your signUp logic here
  //   console.log("hi wtf")
  // }
</script>

<div class={cn("grid gap-6", className)} {...$$restProps}>
  <form on:submit={signUp}>
    <div class="grid gap-2">
      <div class="grid gap-1">
        <Label class="sr-only" for="email">Email</Label>
        <Input
          bind:value={email}
          id="email"
          placeholder="name@example.com"
          type="email"
          autocapitalize="none"
          autocomplete="email"
          autocorrect="off"
        />
      </div>
      <div class="grid gap-1">
        <Label class="sr-only" for="password">Password</Label>
        <Input
          bind:value={password}
          id="password"
          placeholder="password"
          type="password"
          autocapitalize="none"
          autocorrect="off"
        />
      </div>
	  <div class="grid gap-1">
        <Label class="sr-only" for="password2">Password</Label>
        <Input
          bind:value={password2}
          id="password2"
          placeholder="retype password"
          type="password"
          autocapitalize="none"
          autocorrect="off"
        />
      </div>
      <Button type="submit" disabled={isLoading}>
        {#if isLoading}
          <!-- <Icons.spinner class="mr-2 h-4 w-4 animate-spin" /> -->
        {/if}
        Sign Up 
      </Button>
    </div>
  </form>

  <div class="relative">
    <div class="absolute inset-0 flex items-center">
      <span class="w-full border-t" />
    </div>
    <div class="relative flex justify-center text-xs uppercase">
      <span class="bg-background px-2 text-muted-foreground">
        If you already have an account
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
    Log in Here
  </Button>
  </a>
  {#if show_password_alert}
  <Alert.Root variant="destructive">
	<Alert.Title>Wrong Password</Alert.Title>
	<Alert.Description>
	  Both passwords must match
	</Alert.Description>
  </Alert.Root>
  {/if}
  {#if show_error_alert}
  <Alert.Root variant="destructive">
	<Alert.Title>Error Code: {error_alert_code}</Alert.Title>  
  <Alert.Description >
    {error_alert_text}
	</Alert.Description>

  <script lang="ts">
    import { ExclamationTriangle } from "radix-icons-svelte";
    import * as Alert from "$lib/components/ui/alert";
  </script>

</Alert.Root>
  {/if}
</div>
