describe('Quiz Application', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('should start the quiz and navigate through questions', () => {
      // Start the quiz
      cy.get('button').contains('Start').click();
  
      // Verify the first question is displayed
      cy.get('.card h2').should('contain.text', 'Which is the correct answer?');
  
      // Answer the first question
      cy.get('.btn').contains('1').click();
  
      // Verify the second question is displayed
      cy.get('.card h2').should('contain.text', 'Which is the correct answer?');
  
      // Answer the second question
      cy.get('.btn').contains('2').click();
  
      // Verify the third question is displayed
      cy.get('.card h2').should('contain.text', 'Which is the correct answer?');
  
      // Answer the third question
      cy.get('.btn').contains('3').click();
  
      // Verify the quiz is over and score is displayed
      cy.get('.score').should('be.visible');
  
      // Start a new quiz
      cy.get('button').contains('Start New Quiz').click();
  
      // Verify the first question is displayed again
      cy.get('.card h2').should('contain.text', 'Which is the correct answer?');
    });
  });