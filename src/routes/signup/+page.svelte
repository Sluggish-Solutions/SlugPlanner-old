<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import UserAuthForm from "$lib/components/user-auth-signup-form.svelte";
</script>

<!-- <div class="md:hidden">
	<img
		src="/examples/authentication-light.png"
		width={1280}
		height={843}
		alt="Authentication"
		class="block dark:hidden"
	/>
	<img
		src="/examples/authentication-dark.png"
		width={1280}
		height={843}
		alt="Authentication"
		class="hidden dark:block"
	/>
</div> -->
<div
  class="container relative hidden h-[100vh] flex-col items-center justify-center md:grid lg:max-w-none lg:grid-cols-2 lg:px-0"
>
<div class="relative hidden h-full flex flex-col bg-muted p-10 text-black dark:border-r lg:flex">
	<div class="absolute inset-0 bg-cover" style="background-image: url(&quot;https://upload.wikimedia.org/wikipedia/commons/b/be/UCSC_East_Field.jpg&quot;);"></div>
	
	<div class="relative z-20 flex-grow w-full flex flex-col items-center font-medium mx-auto my-auto">
	  <ul class="text-center">
		<li><h2 class="font-bold text-5xl p-6 mt-5 mb-[-3rem] pl-9">Welcome To</h2></li>
		<li><h1 class="font-bold text-[4.7rem] p-3 pl-9  underline decoration-yellow-300 decoration-8">SlugPlanner</h1></li>
		<li class="flex justify-end mt-[-1rem] px-[2rem]">
		  <a href="https://github.com/orgs/Sluggish-Solutions/repositories">
			<h1 class="font-medium" >By Sluggish Solutions</h1>
		</a>
		</li>
		
		<li class="mt-8" >
		  <div class="relative z-20 mt-auto">
			<blockquote class="space-y-2">
			  <p class="text-lg">An easy 4 year planner for fellow slugs!</p>
			  
			</blockquote>
		  </div>
		</li>
	  </ul>
	</div>
  </div>
  
  
  <!-- <div class=" flex justify-center items-center lg:p-8"> -->
  <div class=" flex justify-center items-center">
    <div
      class="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]"
    >
      <div class="flex flex-col space-y-2 text-center">
        <h1 class="text-2xl font-semibold tracking-tight">Create an account</h1>
        <p class="text-sm text-muted-foreground">
          Enter your email below to create your account
        </p>
      </div>
      <UserAuthForm />
      <p class="px-8 text-center text-sm text-muted-foreground">
        By clicking continue, you agree to our{" "}
        <a
          href="/terms"
          class="underline underline-offset-4 hover:text-primary"
        >
          Terms of Service
        </a>{" "}
        and{" "}
        <a
          href="/privacy"
          class="underline underline-offset-4 hover:text-primary"
        >
          Privacy Policy
        </a>
        .
      </p>
    </div>
  </div>
</div>
