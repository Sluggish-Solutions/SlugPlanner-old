<script lang="ts">
  // import { Icons } from "$components/docs";
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import { Label } from "$lib/components/ui/label";
  import { signUpUser } from "$lib/backend/auth";
  import { cn } from "$lib/utils";
  import { stringify } from "postcss";

  let className: string | undefined | null = undefined;
  export { className as class };

  let isLoading = false;

  let email: string;
  let password: string;

  async function onSubmit() {
    isLoading = true;

    setTimeout(() => {
      isLoading = false;
    }, 3000);
  }

  const signUp = async (event: Event) => {
    event.preventDefault();
    // Perform any necessary form validation or other actions before calling signUpUser
    try {
      isLoading = true;
      // Access the email value from the bound variable
      console.log("Email:", email);
      // Call your signUpUser function with the necessary parameters
      console.log(await signUpUser(email, password));
    } catch (error) {
      console.error("Sign up failed:", error);
    } finally {
      isLoading = false;
    }
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
      <Button type="submit" disabled={isLoading}>
        {#if isLoading}
          <!-- <Icons.spinner class="mr-2 h-4 w-4 animate-spin" /> -->
        {/if}
        Sign In with Email
      </Button>
    </div>
  </form>

  <div class="relative">
    <div class="absolute inset-0 flex items-center">
      <span class="w-full border-t" />
    </div>
    <div class="relative flex justify-center text-xs uppercase">
      <span class="bg-background px-2 text-muted-foreground">
        Or continue with
      </span>
    </div>
  </div>
  <Button variant="outline" type="button" disabled={isLoading}>
    {#if isLoading}
      <!-- <Icons.spinner class="mr-2 h-4 w-4 animate-spin" /> -->
    {:else}
      <!-- <Icons.git Hub class="mr-2 h-4 w-4" /> -->
    {/if}
    {" "}
    Github
  </Button>
</div>
