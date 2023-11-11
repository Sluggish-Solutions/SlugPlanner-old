<script>
    // You can export any props that your component might accept
    import { Terminal } from "lucide-svelte";
    import * as Alert from "$lib/components/ui/alert";
    
    export let row1 = 'Row 1';
    export let row2 = 'Row 2';
    export let row3 = 'Row 3';
    export let row4 = 'Row 4';
  </script>
<div
class="rounded-xl w-[rem] px-10
 flex items-start border bg-card text-card-foreground shadow"
>
  <Alert.Root class="w-[10rem]">
    <!-- <Terminal class="h-4 w-4" /> -->
    <Alert.Title class="text-center">Heads up!</Alert.Title>
    <Alert.Description>
      <ul>
        
        <li>{row1}</li>
        <li>{row2}</li>
        <li>{row3}</li>
        <li>{row4}</li>
      </ul>
    </Alert.Description>
  </Alert.Root>
  </div>