import { createClient } from '@supabase/supabase-js'

import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY } from '$env/static/public'
export const supabase = createClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY)
// export const supabase = createClient("https://pzjklwrhzjnmjxgojsul.supabase.co/","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB6amtsd3JoempubWp4Z29qc3VsIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTk1MTkxMTYsImV4cCI6MjAxNTA5NTExNn0.zDv6orTxDDa4o54B-m9bGd4j-OoNPnTyUytunBh2q_c")