from flask import jsonify, request, abort
from app import db
from app.models import Symptom, Disease, SymptomDisease
import traceback

def register_routes(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'The request was invalid or cannot be processed.'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'The requested resource could not be found.'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'An unexpected error occurred. We are looking into it!'
        }), 500

    @app.route('/symptoms')
    def get_symptoms():
        try:
            symptoms = Symptom.query.all()
            return jsonify({'success': True, 'symptoms': [{'id': s.id, 'name': s.name, 'description': s.description} for s in symptoms]})
        except Exception as e:
            app.logger.error(f"Error fetching symptoms: {str(e)}")
            return jsonify({'success': False, 'error': 500, 'message': 'Failed to retrieve symptoms. Please try again later.'}), 500

    @app.route('/diseases')
    def get_diseases():
        try:
            diseases = Disease.query.all()
            return jsonify({'success': True, 'diseases': [{'id': d.id, 'name': d.name, 'category': d.category} for d in diseases]})
        except Exception as e:
            app.logger.error(f"Error fetching diseases: {str(e)}")
            return jsonify({'success': False, 'error': 500, 'message': 'Failed to retrieve diseases. Please try again later.'}), 500

    @app.route('/diagnose', methods=['POST'])
    def diagnose():
        try:
            data = request.json
            if not data or 'symptoms' not in data:
                return jsonify({'success': False, 'error': 400, 'message': 'Please provide symptom data for diagnosis.'}), 400
                
            symptom_names = data.get('symptoms')
            if not symptom_names:
                return jsonify({'success': False, 'error': 400, 'message': 'At least one symptom is required for diagnosis.'}), 400

            symptoms = Symptom.query.filter(Symptom.name.in_(symptom_names)).all()
            if not symptoms:
                return jsonify({'success': False, 'error': 404, 'message': 'None of the provided symptoms were found in our database.'}), 404

            possible_diseases = []
            for symptom in symptoms:
                for assoc in symptom.disease_associations:
                    possible_diseases.append({
                        'disease': assoc.disease.name, 
                        'probability': assoc.probability
                    })
            
            return jsonify({'success': True, 'possible_diseases': possible_diseases})
        except Exception as e:
            app.logger.error(f"Error during diagnosis: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'success': False, 'error': 500, 'message': 'We encountered an issue while diagnosing. Please try again, or contact support if the issue persists.'}), 500

# Add similar error handling for other routes as they are implemented
