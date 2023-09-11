from supabase import Client

from Services.States.ServicesState import ServicesState


def UpdateStateOfScheduleService(supabase: Client, service: str):
    response = (
        supabase.table("Services")
        .update({
            'State': ServicesState.SCHEDULE.name,
        })
        .eq('Process', service)
        .execute()
    )
    if len(response.data) == 1:
        return {
            'Error': False,
            'Message': 'Successful'
        }
    else:
        return {
            'Error': True,
            'Message': 'Cannot update the state of service'
        }
