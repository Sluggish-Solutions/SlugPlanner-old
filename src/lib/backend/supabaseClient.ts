import { createClient } from '@supabase/supabase-js'
import * as keys from "$lib/backend/keys"
export const supabase = createClient(keys.get_url(), keys.get_key())


export async function load(){
    const {data} = await supabase.from("all_classes").select();
    return {
        classes: data ?? [],
    };
}