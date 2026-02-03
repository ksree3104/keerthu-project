from django.core.management.base import BaseCommand
from pro.models import Product, Client, FabricationProcess, MaterialAdvisor

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Product population removed - users should add products manually via admin panel
        
        # Create sample clients
        clients_data = [
            {
                'name': 'Rajesh Kumar',
                'company': 'Indian Railways',
                'email': 'rajesh.kumar@indianrailways.gov.in',
                'phone': '+91-9876543210',
                'industry': 'railway'
            },
            {
                'name': 'Priya Sharma',
                'company': 'Metro Rail Corporation',
                'email': 'priya.sharma@metro.in',
                'phone': '+91-9876543211',
                'industry': 'railway'
            },
            {
                'name': 'Amit Patel',
                'company': 'Automotive Solutions Ltd',
                'email': 'amit.patel@auto.in',
                'phone': '+91-9876543212',
                'industry': 'automotive'
            },
            {
                'name': 'Sunita Singh',
                'company': 'Engineering Works',
                'email': 'sunita.singh@engworks.in',
                'phone': '+91-9876543213',
                'industry': 'engineering'
            }
        ]

        for client_data in clients_data:
            Client.objects.get_or_create(
                email=client_data['email'],
                defaults=client_data
            )

        # Create fabrication processes
        processes_data = [
            {
                'name': 'Cutting',
                'description': 'Precision cutting of metal sheets using CNC machines',
                'time_minutes': 2.0,
                'cost_per_unit': 280.00,
                'quality_score': 1
            },
            {
                'name': 'Bending',
                'description': 'Metal bending and forming operations',
                'time_minutes': 3.0,
                'cost_per_unit': 500.00,
                'quality_score': 1
            },
            {
                'name': 'Welding',
                'description': 'TIG/MIG welding for structural integrity',
                'time_minutes': 5.0,
                'cost_per_unit': 1000.00,
                'quality_score': 2
            },
            {
                'name': 'Polishing',
                'description': 'Surface finishing and polishing',
                'time_minutes': 2.0,
                'cost_per_unit': 1500.00,
                'quality_score': 1
            },
            {
                'name': 'Assembly',
                'description': 'Final assembly and quality inspection',
                'time_minutes': 4.0,
                'cost_per_unit': 400.00,
                'quality_score': 2
            }
        ]

        for process_data in processes_data:
            FabricationProcess.objects.get_or_create(
                name=process_data['name'],
                defaults=process_data
            )

        # Create material advisor data
        advisors_data = [
            {
                'environment': 'coastal',
                'weight_sensitivity': 'medium',
                'budget': 'standard',
                'finish_preference': 'mirror',
                'recommended_material': 'Stainless Steel',
                'reasoning': 'Coastal environment requires corrosion resistance. Stainless steel provides excellent protection against salt air.',
                'tradeoffs': 'Higher cost and weight compared to aluminium.'
            },
            {
                'environment': 'indoor',
                'weight_sensitivity': 'high',
                'budget': 'tight',
                'finish_preference': 'brushed',
                'recommended_material': 'Aluminium',
                'reasoning': 'Indoor use with weight constraints and budget considerations make aluminium ideal.',
                'tradeoffs': 'Less durable than stainless steel for harsh environments.'
            }
        ]

        for advisor_data in advisors_data:
            MaterialAdvisor.objects.get_or_create(
                environment=advisor_data['environment'],
                weight_sensitivity=advisor_data['weight_sensitivity'],
                budget=advisor_data['budget'],
                finish_preference=advisor_data['finish_preference'],
                defaults=advisor_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data'))